page = ("""<li class="nav-item dropdown">
					<a class="nav-link" id="navbarDropdown1" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false" href="#">Services</a>
					<ul class="list-unstyled dropdown-menu" aria-labelledby="navbarDropdown1">
						<li class="nav-item text-center">
							<a href="web-design-services.html">Web Design</a>
						</li>
						<li class="nav-item text-center">
							<a href="mobile-app-development.html">""")
start_link = page.find('<a href=')
start_quote = page.find('"', start_link)
end_quote = page.find('"', start_quote + 1)
url = page[start_quote + 1 : end_quote]

print (url)
print (start_quote + 1)
print (end_quote)