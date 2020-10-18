from wtforms import Form, StringField, TextAreaField, IntegerField


class PostFormBlog(Form):
	title = StringField('Title')
	img_path = StringField('Img_path')
	tags = StringField('Tags')
	text = TextAreaField('Text')


class PostComments(Form):
	name = StringField('Name')
	text = TextAreaField('Text')



