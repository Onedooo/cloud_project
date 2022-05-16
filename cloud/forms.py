from django.forms import forms
from django import forms

from cloud.models import FileDetailInfo, UserInfo, Comment


class FileUploadForm(forms.ModelForm):
	class Meta:
		model = FileDetailInfo
		fields = ['file_title', 'file_upload', 'guest_name', 'file_url', ]
		labels ={
			'file_title': '파일명',
			'file_upload': '업로드일자',
			'guest_name': '공유명단',
			'file_url': '파일선택',
		}


class FileEditForm(forms.ModelForm):
	class Meta:
		model = FileDetailInfo
		fields = ['file_title','guest_name', 'file_url', ]
		labels = {'file_title': '파일명','guest_name': '공유명단', 'file_url': '파일선택', }


class UserEditForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['phone_num', ]


class UserForm(forms.ModelForm):
	class Meta:
		model = UserInfo
		fields = ['name', 'email', 'phone_num',]


class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['comment_text',]
		labels = {'comment_text': '',}
