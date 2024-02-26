from jinja2 import Environment as JinjaEnv, FileSystemLoader as JinjaFS
from markdown2 import Markdown as MDEnv

__TemplateRenderer__ = JinjaEnv(loader=JinjaFS(searchpath="./views"))

def RenderTemplate(TemplateFileName: str, *args, **kwargs):
    """Renders a Jinja2 template from a file."""
    return __TemplateRenderer__.get_template(TemplateFileName).render(*args, **kwargs)

__MDRenderer__ = MDEnv(extras=["header-ids", "metadata", "markdown-in-html", "code-friendly", "footnotes", "fenced-code-blocks", "strike"], footnote_title="Jump back to footnote %d in the text.", footnote_return_symbol="&#8617;")

def RenderMarkdown(MDSource: str):
    """Renders Markdown, but pre-configured."""
    return __MDRenderer__.convert(MDSource)

