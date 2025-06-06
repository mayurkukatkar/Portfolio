from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import (
    Profile, Project, Skill, Experience, 
    Testimonial, Blog, ContactSubmission, GlobalSetting
)

# Create your views here.

def get_global_context():
    """Get global context data for all templates"""
    try:
        global_settings = GlobalSetting.objects.first()
    except GlobalSetting.DoesNotExist:
        global_settings = None
    
    try:
        profile = Profile.objects.first()
    except Profile.DoesNotExist:
        profile = None
    
    return {
        'global_settings': global_settings,
        'profile': profile,
    }

def home(request):
    """Home page view"""
    context = get_global_context()
    context.update({
        'projects': Project.objects.all()[:3],  # Latest 3 projects
        'skills': Skill.objects.all()[:6],      # Top 6 skills
        'testimonials': Testimonial.objects.all()[:3],  # Latest 3 testimonials
    })
    return render(request, 'portfolio_app/home.html', context)

def about(request):
    """About page view"""
    context = get_global_context()
    return render(request, 'portfolio_app/about.html', context)

def projects(request):
    """Projects listing page view"""
    context = get_global_context()
    projects_list = Project.objects.all()
    
    # Filter by tag if provided
    tag = request.GET.get('tag')
    if tag:
        projects_list = projects_list.filter(tags__icontains=tag)
    
    context.update({
        'projects': projects_list,
        'selected_tag': tag,
    })
    return render(request, 'portfolio_app/projects.html', context)

def project_detail(request, pk):
    """Project detail page view"""
    context = get_global_context()
    project = get_object_or_404(Project, pk=pk)
    context.update({
        'project': project,
    })
    return render(request, 'portfolio_app/project_detail.html', context)

def skills(request):
    """Skills page view"""
    context = get_global_context()
    skills_list = Skill.objects.all()
    
    # Group skills by category
    skills_by_category = {}
    for skill in skills_list:
        if skill.category not in skills_by_category:
            skills_by_category[skill.category] = []
        skills_by_category[skill.category].append(skill)
    
    context.update({
        'skills_by_category': skills_by_category,
    })
    return render(request, 'portfolio_app/skills.html', context)

def experience(request):
    """Experience page view"""
    context = get_global_context()
    
    # Get work and education experiences
    work_experience = Experience.objects.filter(type='work')
    education = Experience.objects.filter(type='edu')
    
    context.update({
        'work_experience': work_experience,
        'education': education,
    })
    return render(request, 'portfolio_app/experience.html', context)

def blog(request):
    """Blog listing page view"""
    context = get_global_context()
    blog_posts = Blog.objects.all()
    
    # Filter by tag if provided
    tag = request.GET.get('tag')
    if tag:
        blog_posts = blog_posts.filter(tags__icontains=tag)
    
    context.update({
        'blog_posts': blog_posts,
        'selected_tag': tag,
    })
    return render(request, 'portfolio_app/blog.html', context)

def blog_detail(request, slug):
    """Blog detail page view"""
    context = get_global_context()
    blog_post = get_object_or_404(Blog, slug=slug)
    
    # Get related posts based on tags
    tags = [tag.strip() for tag in blog_post.tags.split(',')]
    related_posts = Blog.objects.exclude(pk=blog_post.pk)
    
    for tag in tags:
        related_posts = related_posts.filter(tags__icontains=tag)
    
    context.update({
        'blog_post': blog_post,
        'related_posts': related_posts[:3],  # Limit to 3 related posts
    })
    return render(request, 'portfolio_app/blog_detail.html', context)

def testimonials(request):
    """Testimonials page view"""
    context = get_global_context()
    context.update({
        'testimonials': Testimonial.objects.all(),
    })
    return render(request, 'portfolio_app/testimonials.html', context)

def contact(request):
    """Contact page view with form handling"""
    context = get_global_context()
    
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        
        if name and email and message:
            # Save the contact submission
            ContactSubmission.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('portfolio:contact')
        else:
            messages.error(request, 'Please fill in all required fields.')
    
    return render(request, 'portfolio_app/contact.html', context)
