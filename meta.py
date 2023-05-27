HEADER_INFO = """""".strip()
SIDEBAR_INFO = """
<div class="contributors font-body text-bold">
<a class="contributor comma" href="https://huggingface.co/m3hrdadfi">TEAM 8</a>


</div>
"""
CHEF_INFO = """
<h2 class="font-title">Welcome to  Crazy  Restaurant! </h2>
<p class="strong font-body">
<span class="d-block extra-info">(We are at your service with two of the best chefs in the world: Chef Traditional, 
Chef Modern. Moedern is known for being more creative whereas Traditiional is more meticulous.)</span>
</p>
""".strip()
PROMPT_BOX = "Add custom ingredients here (separated by `,`): "
STORY = """
<div class="story-box font-body">
<p>
Hello everyone 👋, I am <strong>Maaster Chef </strong>, 
the owner of this restaurant.  Ask me anything about cooking

</p>

<pre>[Inputs]
    {food items*: separated by comma}
     
[Targets]
    title: {TITLE} &lt;section>
    ingredients: {INGREDIENTS: separated by &lt;sep>} &lt;section>
    directions: {DIRECTIONS: separated by &lt;sep>}.
</pre>

<p>
  <em>In the cookbooks (a.k.a <a href="https://huggingface.co/datasets/recipe_nlg">dataset</a>), the food items were referred to as NER. </em>
</p>
<p>
 
</p>

</div>
""".strip()
