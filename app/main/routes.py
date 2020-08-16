from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g, \
    jsonify, current_app, session
from flask_login import current_user, \
    login_required  # current_user returns the data corresponding to the logged in user relative to the User model (Global method)
from flask_babel import _, get_locale
from guess_language import guess_language
from app import db
from app.main.forms import EditProfileForm, PostForm, MessageForm, CodeForm, ChatForm, TextForm
from app.models import User, Post, Message, Notification
from app.translate import translate
from app.main import bp
import numpy as np
from sklearn.preprocessing import normalize
import io
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import Algorithmia


@bp.route('/', methods=['GET', 'POST'])
@bp.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        language = guess_language(form.post.data)
        if language == 'UNKNOWN' or len(language) > 5:
            language = ''
        post = Post(body=form.post.data, author=current_user,
                    language=language)
        db.session.add(post)
        db.session.commit()
        flash(_('Your post is now live!'))
        return redirect(url_for('main.index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('main.index', page=posts.prev_num) \
        if posts.has_prev else None



    return render_template('index.html', title=_('Home'), form=form,
                           posts=posts.items, next_url=next_url,
                           prev_url=prev_url)


@bp.route('/explore/<username>', methods=['GET', 'POST'])
@login_required
def explore(username):
    user = User.query.filter_by(username=username).first_or_404()
    form = CodeForm()
    if form.validate_on_submit():
        current_user.code = form.code.data

        current_user.experience = form.experience.data
        current_user.performance = form.performance.data
        current_user.cohesion = form.cohesion.data
        current_user.communication = form.communication.data
        current_user.balance = form.balance.data
        current_user.balance_extra = form.balance_extra.data
        current_user.comments = form.comments.data
        current_user.improve = form.improve.data
        current_user.keep = form.keep.data
        current_user.other = form.other.data
        current_user.satisfaction = form.satisfaction.data
        ## TIPI
        current_user.enthusiasm = form.enthusiasm.data
        current_user.critical = form.critical.data
        current_user.dependable = form.dependable.data
        current_user.anxious = form.anxious.data
        current_user.complex = form.complex.data
        current_user.reserved = form.reserved.data
        current_user.warm = form.warm.data
        current_user.careless = form.careless.data
        current_user.calm = form.calm.data
        current_user.uncreative = form.uncreative.data

        flash(_('Your code has been submitted! Thank you!'))
        db.session.commit()

        print(current_user, current_user.code)
        return 'Your code has been submitted, thank you for your participation! We will reward you shortly.'
    """Chat room. The user's name and room must be stored in
        the session."""
    name = session.get('name', '')
    room = session.get('room', '')
    if name == '' or room == '':
        return redirect(url_for('main.explore'))

    textform = TextForm()


    return render_template('explore.html', title=_('Explore'), form=form, user=user, username=username, name=name,
                           room=room, textform=textform)


@bp.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('main.explore', page=posts.next_num, username=username) \
        if posts.has_next else None
    prev_url = url_for('main.explore', page=posts.prev_num, username=username) \
        if posts.has_prev else None

    ####### START Tranform scores to integers ########

    def transform_score(score):

        if score == 'Very Low':
            score = 1
        elif score == 'Low':
            score = 2
        elif score == 'Moderate':
            score = 3
        elif score == 'Good':
            score = 4
        elif score == 'High':
            score = 5

            return score
        return score

    users = User.query.all()

    participants = []
    for u in users:
        if u.username != 'Admin':
            participants.append(u)
    how_many = len(participants)
    users_data = ([])
    iter_results = []

    for i in users:
        i.extraversion = (transform_score(i.extra)) + (transform_score(i.art))
        i.agreeableness = (transform_score(i.trust)) + (transform_score(i.fault))
        i.conscientiousness = (transform_score(i.lazy)) + (transform_score(i.job))
        i.neuroticism = (transform_score(i.relax)) + (transform_score(i.nervous))
        i.openness = (transform_score(i.social)) + (transform_score(i.imagination))
        i.ability = transform_score(i.ability)
        i.match = None
        db.session.commit()
        i.user_list = [i.extraversion, i.agreeableness, i.conscientiousness, i.neuroticism, i.openness, i.ability]
        i.user_array = np.asarray(i.user_list)
        i.user_array = [int(numeric_string) for numeric_string in i.user_array]
        users_data.append(i.user_array)
        i.user_array = np.sqrt(i.user_array)  # sqrt of other users array
        i.user_array = normalize(i.user_array[:, np.newaxis], axis=0).ravel()

        # get difference of current_user's array to users arrays
        # https://stackoverflow.com/questions/30024612/calculating-similarity-between-two-profiles-for-number-of-common-features
    current_user.user_list = [transform_score(current_user.extraversion), transform_score(current_user.agreeableness),
                              transform_score(current_user.conscientiousness),
                              transform_score(current_user.neuroticism), transform_score(current_user.openness), transform_score(current_user.ability)]
    current_user.user_array = np.array(current_user.user_list)
    current_user.user_array = [int(numeric_string) for numeric_string in current_user.user_array]
    current_user.user_array = np.sqrt(current_user.user_array)  # sqrt of current user array
    current_user.user_array = normalize(current_user.user_array[:, np.newaxis], axis=0).ravel()

    ####### END Tranform scores to integers ########

    ####### START Euclidian distance between users arrays ########

    def first_index(results):
        return results[0]

    def third_index(results):
        return results[2]

    ### Slice user table into chunks of 8

    for i in users:
        for x in users:
            if x != i and i.username !='Admin' and x.username != 'Admin':
                result = 100 - (np.linalg.norm(x.user_array - i.user_array)) * 100
                result_with_percentage = result
                iter_user_tuple = (i.username, x.username, result_with_percentage)
                iter_results.append(iter_user_tuple)

    iter_ordered_results = sorted(iter_results, key=third_index, reverse=True)
    print(iter_ordered_results)
    iter_reversed_results = sorted(iter_results, key=third_index, reverse=False)
    iter_randomised_results = sorted(iter_results, key=first_index)

    def pop_third_element(iter_ordered_results):

        ordered = []
        for x in iter_ordered_results:
            x = list(x)
            x.pop(2)
            ordered.append(x)
        iter_ordered_results = tuple(ordered)
        return iter_ordered_results

    iter_ordered_results = pop_third_element(iter_ordered_results)
    iter_reversed_results = pop_third_element(iter_reversed_results)
    iter_randomised_results = pop_third_element(iter_randomised_results)

    def transform_to_dict(iter_ordered_results):
        groups = {}
        for number, string in iter_ordered_results:
            groups.setdefault(number, []).extend(["{}".format(string)])
        input = {"preferences": groups}
        return input

    input = transform_to_dict(iter_ordered_results)
    input_reversed = transform_to_dict(iter_reversed_results)
    input_randomised = transform_to_dict(iter_randomised_results)

    # input = {key:val for key, val in input.items() if val != user.match}

    ####### END Euclidian distance between users arrays ########

    ####### START Stable Matchmaking ########

    def algorithmia(input):
        client = Algorithmia.client('simYxB74zyJL00QetJW1Ca8RU8V1')
        algo = client.algo('matching/StableRoommateAlgorithm/0.1.1')
        algo.set_options(timeout=300)  # optional
        input = algo.pipe(input).result
        return input

    threshold = 4

    if len(participants) >= threshold and (len(participants)) % 2 == 0 :
        ordered_stable_match = algorithmia(input)

        # reversed_stable_match = algorithmia(input_reversed)
        # randomised_stable_match = algorithmia(input_randomised)

        def getUnique(dictionary_matches):
            result = {}
            for key, value in dictionary_matches.items():
                if value not in result.values() and value not in result.keys():
                    result[key] = value
            return result

        unique_ordered_match = getUnique(ordered_stable_match)
        print(unique_ordered_match, len(unique_ordered_match))
        matched_pairs = len(unique_ordered_match)
        # unique_reversed_match = getUnique(reversed_stable_match)
        # unique_random_match = getUnique(randomised_stable_match)
        #
        # list_of_matches = [unique_ordered_match, unique_reversed_match, unique_random_match]

        # random.shuffle(list_of_matches)

        defuser = 'Defuser'
        lead_expert = 'Lead Expert'
        for user in users:
            for key, value in unique_ordered_match.items():
                if user.username == key:
                    user.role = lead_expert
                    db.session.commit()

                elif user.username == value:
                    user.role = defuser
                    db.session.commit()
            print(user.username, user.role)

        for user in users:
            for key, value in unique_ordered_match.items():
                if key == user.username:
                    user.match = value
                    user.room = key + value
                    db.session.commit()
                elif value == user.username:
                    user.match = key
                    user.room = key + value
                    db.session.commit()

    else:

        user.match = 'waiting for a match'
        user.room = 'not yet decided'
        user.role = 'not yet decided'
        db.session.commit()
        matched_pairs = 0

    ####### END Stable Matchmaking ########


    # elif request.method == 'GET':
    #     form.name.data = session.get('name', '')
    #     form.room.data = session.get('room', '')

    session['name'] = current_user.username
    session['room'] = 'common'

    textform = TextForm()


    form = ChatForm()
    if form.validate_on_submit():
        session['name'] = current_user.username
        session['room'] = current_user.room
        return redirect(url_for('main.explore', username=username))
    elif request.method == 'GET':
        form.name.data = session.get('name', '')
        form.room.data = session.get('room', '')





    return render_template('user.html', user=user, posts=posts.items,
                           next_url=next_url, prev_url=prev_url,
                           match=current_user.match, users=users, how_many=how_many, matched_pairs=matched_pairs,
                           form=form, threshold=threshold, textform=textform)





@bp.route('/user/<username>/popup', methods=['GET', 'POST'])
@login_required
def user_popup(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user_popup.html', user=user)


@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash(_('Your changes have been saved.'))
        return redirect(url_for('main.edit_profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me

    return render_template('edit_profile.html', title=_('Edit Profile'),
                           form=form)


@bp.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot follow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    flash(_('You are following %(username)s!', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash(_('User %(username)s not found.', username=username))
        return redirect(url_for('main.index'))
    if user == current_user:
        flash(_('You cannot unfollow yourself!'))
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    flash(_('You are not following %(username)s.', username=username))
    return redirect(url_for('main.user', username=username))


@bp.route('/translate', methods=['POST'])
@login_required
def translate_text():
    return jsonify({'text': translate(request.form['text'],
                                      request.form['source_language'],
                                      request.form['dest_language'])})


@bp.route('/send_message/<recipient>', methods=['GET', 'POST'])
@login_required
def send_message(recipient):
    user = User.query.filter_by(username=recipient).first_or_404()
    form = MessageForm()
    page = request.args.get('page', 1, type=int)

    if form.validate_on_submit():
        msg = Message(author=current_user, recipient=user,
                      body=form.message.data)
        db.session.add(msg)

        user.add_notification('unread_message_count', user.new_messages())
        db.session.commit()


    else:
        msg = 'Waiting for the first message!'

    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    messages_sent = current_user.messages_sent.order_by(
        Message.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)
    form.message.data = ""

    return render_template('send_message.html', title=_('Send Message'),
                           form=form, user=user, msg=msg, messages=messages.items,
                           messages_sent=messages_sent.items, username=recipient)


@bp.route('/messages')
@login_required
def messages():
    current_user.last_message_read_time = datetime.utcnow()
    current_user.add_notification('unread_message_count', 0)
    db.session.commit()
    page = request.args.get('page', 1, type=int)
    messages = current_user.messages_received.order_by(
        Message.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    messages_sent = current_user.messages_sent.order_by(
        Message.timestamp.desc()).paginate(
        page, current_app.config['POSTS_PER_PAGE'], False)

    next_url = url_for('main.messages', page=messages.next_num) \
        if messages.has_next else None
    prev_url = url_for('main.messages', page=messages.prev_num) \
        if messages.has_prev else None
    return render_template('messages.html', messages=messages.items,
                           next_url=next_url, prev_url=prev_url, messages_sent=messages_sent.items)


@bp.route('/export_posts')
@login_required
def export_posts():
    if current_user.get_task_in_progress('export_posts'):
        flash(_('An export task is currently in progress'))
    else:
        current_user.launch_task('export_posts', _('Exporting posts...'))
        db.session.commit()
    return redirect(url_for('main.user', username=current_user.username))


@bp.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])
