from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from . forms import PostForm, CommentForm, ReplyForm, PostLikeForm, CommentLikeForm, ReplyLikeForm
from . models import Post, Comment, Reply, PostLike, CommentLike, ReplyLike
from blogs.models import Blog
from events.models import Event
from django.core.paginator import Paginator



# Create your views here.
@login_required(redirect_field_name='next', login_url='signin')
def communityWall(request):

    # Pre action variables

    # calling Post obj and seting up paginator
    posts = Post.objects.all()

    page = request.GET.get('page', 1) # this set page to equal page 1
    paginator = Paginator(posts, 4) # this breaks posts obj into groups of 4
    posts = paginator.get_page(page) # this resets posts to equal paginator page 1

    # call rest of user entries
    comments = Comment.objects.all()
    replies = Reply.objects.all()

    blogs = Blog.objects.all()
    blog_length = len(blogs)
    first_blogs = []
    if blog_length >= 3:
        for i in range(3):
            first_blogs.append(blogs[i])
    else:
        for i in range(blog_length):
            first_blogs.append(blogs[i])

    events = Event.objects.all()
    event_length = len(events)
    first_events = []
    if event_length >= 3:
        for i in range(3):
            first_events.append(events[i])
    else:
        for i in range(event_length):
            first_events.append(events[i])


    # call user likes
    post_likes = PostLike.objects.all()
    comment_likes = CommentLike.objects.all()
    reply_likes = ReplyLike.objects.all()

    # create user Post like list to deal with like button ~ deactivate
    user_post_likes = []
    upl = PostLike.objects.filter(user=request.user)
    for post in upl:
        user_post_likes.append(post.post)

    # create user Comment like list to deal with like button ~ deactivate
    user_comment_likes = []
    ucl = CommentLike.objects.filter(user=request.user)
    for comment in ucl:
        user_comment_likes.append(comment.comment)

    # create user Reply like list to deal with like button ~ deactivate
    user_reply_likes = []
    urll = ReplyLike.objects.filter(user=request.user)
    for reply in urll:
        user_reply_likes.append(reply.reply)


    # Post Logic
    if 'post' in request.POST:
        if request.POST.get('create_post') == 'post':
            postform = PostForm(data=request.POST, files=request.FILES)
            if postform.is_valid():
                new_post = postform.save(commit=False)
                if request.POST.get('post_image'):
                    new_post.post_image = request.FILES['post_image']
                new_post.save()
            return redirect('communityWall') # redirect so if user hits refresh it doesnt resubmit

    # Comment logic
    if 'comment' in request.POST:
        if request.POST.get('create_comment') == 'comment':
            commentform = CommentForm(request.POST)
            if commentform.is_valid():
                current_post = Post.objects.filter(id=request.POST.get('parent_id'))
                new_comment = commentform.save(commit=False)
                new_comment.post = current_post[0]
                new_comment.save()
            return redirect('communityWall')

    # Reply Logic
    if 'reply' in request.POST:
        if request.POST.get('create_reply') == 'reply':
            replyform = ReplyForm(request.POST)
            if replyform.is_valid():
                current_comment = Comment.objects.filter(id=request.POST.get('parent_id'))
                new_reply = replyform.save(commit=False)
                new_reply.comment = current_comment[0]
                new_reply.save()
            return redirect('communityWall')

    # Post Like logic
    if 'post_like' in request.POST:
        if request.POST.get('like_post') == 'post_like':
            post_like_form = PostLikeForm(request.POST)
            if post_like_form.is_valid():
                new_like = post_like_form.save(commit=False)
                new_like.post = Post.objects.get(id=request.POST.get('post_id_like'))
                new_like.user = request.user
                new_like.save()
            post = Post.objects.get(id=request.POST.get('post_id_like'))
            post.like_count += 1
            post.save()
            return redirect('communityWall')

    # Comment Like logic
    if 'comment_like' in request.POST:
        if request.POST.get('like_comment') == 'comment_like':
            comment_like_form = CommentLikeForm(request.POST)
            if comment_like_form.is_valid():
                new_like = comment_like_form.save(commit=False)
                new_like.comment = Comment.objects.get(id=request.POST.get('comment_id_like'))
                new_like.user = request.user
                new_like.save()
            comment = Comment.objects.get(id=request.POST.get('comment_id_like'))
            comment.like_count += 1
            comment.save()
            return redirect('communityWall')

    # Reply Like logic
    if 'reply_like' in request.POST:
        if request.POST.get('like_reply') == 'reply_like':
            reply_like_form = ReplyLikeForm(request.POST)
            if reply_like_form.is_valid():
                new_like = reply_like_form.save(commit=False)
                new_like.reply = Reply.objects.get(id=request.POST.get('reply_id_like'))
                new_like.user = request.user
                new_like.save()
            reply = Reply.objects.get(id=request.POST.get('reply_id_like'))
            reply.like_count += 1
            reply.save()
            return redirect('communityWall')

    post_like_form = PostLikeForm()
    comment_like_form = CommentLikeForm()
    reply_like_form = ReplyLikeForm()
    postform = PostForm(initial = {'author': request.user})
    commentform = CommentForm(initial = {'author': request.user, 'post': 1})
    replyform = ReplyForm(initial = {'author': request.user, 'comment': 1})# Change to 1 and never delete first comment

    context = {
        'posts': posts,
        'postform': postform,
        'post_like_form': post_like_form,
        'post_likes': post_likes,
        'comments': comments,
        'commentform': commentform,
        'comment_like_form': comment_like_form,
        'comment_likes': comment_likes,
        'replies': replies,
        'replyform': replyform,
        'reply_like_form': reply_like_form,
        'reply_likes': reply_likes,
        'user_post_likes': user_post_likes,
        'user_comment_likes': user_comment_likes,
        'user_reply_likes': user_reply_likes,
        'first_blogs': first_blogs,
        'first_events': first_events,
    }

    return render(request, 'home.html', context)
