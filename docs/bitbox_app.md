---
layout: default
title: BitBox App
nav_order: 5
nav_exclude: false

---

# {{page.title}}
{: .no_toc }


These guides are still being written, please stay tuned.


{% for object in site.data.guide.guide limit:20%}
{% for x in object %}
{% if x contains "title" %}
## Level 1
### Quesion: {{x.title}}
Answer: {{x.text}}
{% continue %}
{% endif %}
{% for y in x %}
{% for z in y %}
{% if z contains "title" %}
### Level 3
### Quesion: {{z.title}}
Answer: {{z.text}}
{% endif %}
{% endfor %}  
{% endfor %}  
{% endfor %}  
{% endfor %}  
