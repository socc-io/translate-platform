from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from parser.html_parser import parse as html_parse

from django.contrib.auth.models import User, Group
from transi.models import Document, Paragraph, Translated
from rest_framework import viewsets

from transi.serializers import UserSerializer, GroupSerializer, \
	DocumentSerializer, \
	ParagraphSerializer, \
	TranslatedSerializer
from transi.models import Document, Paragraph, Translated

@api_view(['POST'])
def post_html(req):
	if req.method == 'POST':
		try:
			title = req.data['title']
			content = req.data['content']
			original_lang = req.data['original_lang']
			target_lang = req.data['target_lang']
		except:
			return Response({'success': 0, 'error': u'잘못된 요청입니다'})
		try:
			pairs = html_parse(str(content))
		except:
			return Response({'success': 0, 'error': u'컨텐츠 파싱에 실패했습니다'})
		try:
			document = Document.objects.create(owner=req.user, title=title, original_lang=original_lang,\
				target_lang=target_lang)
			for pair in pairs:
				translatee = content[pair[0]:pair[1]]
				Paragraph.objects.create(document=document, content=translatee)
			return Response({'success': 1, \
				'document': DocumentSerializer(document, context={'request': req}).data})
		except Exception as e:
			print(e)
			return Response({'success': 0, 'error': u'오브젝트 생성에 실패했습니다'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
class DocumentViewSet(viewsets.ModelViewSet):
	queryset = Document.objects.all() 
	serializer_class = DocumentSerializer

class ParagraphViewSet(viewsets.ModelViewSet):
	queryset = Paragraph.objects.all()
	serializer_class = ParagraphSerializer

class TranslatedViewSet(viewsets.ModelViewSet):
	queryset = Translated.objects.all()
	serializer_class = TranslatedSerializer