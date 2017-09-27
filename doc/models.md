# Text-related objects
Document - Paragraph가 1-many
Paragraph - Translated가 1-many
로 되어있습니다.

### Document
``` python3
class Document(models.Model):
	owner = models.ForeignKey(User)
	title = models.CharField(max_length=200)
	created_date = models.DateTimeField(default=timezone.now)
	original_lang = models.CharField(max_length=10)
	target_lang = models.CharField(max_length=10)
```
문서 하나당 Document하나에 해당합니다.

### Paragraph
``` python3
class Paragraph(models.Model):
	document = models.ForeignKey(Document)
	content = models.TextField()
```
Document에서 추출된 문단 하나 당 하나의 Paragraph로 대응됩니다.

### Translated
``` python3
class Translated(models.Model):
	paragraph = models.ForeignKey(Paragraph)
	content = models.TextField()
	target_lang = models.CharField(max_length=10)
```
Paragraph가 번역된 문장은 Translated가 저장합니다