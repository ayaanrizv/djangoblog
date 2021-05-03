from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'author', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title here.'}),
			'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title-tag here.'}),
			'author': forms.Select(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your post here.'}),

		}

class EditForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ('title', 'title_tag', 'body')

		widgets = {
			'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title here.'}),
			'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title-tag here.'}),
			#'author': forms.Select(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your post here.'}),

		}

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ('name', 'body')

		widgets = {
			'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title here.'}),
			#'title_tag': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the title-tag here.'}),
			#'author': forms.Select(attrs={'class':'form-control'}),
			'body': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your post here.'}),

		}