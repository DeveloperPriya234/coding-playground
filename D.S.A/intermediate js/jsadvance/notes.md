what is the dom?**(client side
document object model)
*DOM as a tree like structure
*different between DOM and HTML
*`document`object and how javascript interacts with the DOM

---

### **2.selecting Elements**

#### Basic selections:

*`documents. getElementsBy.Id{}`
*`document.getElementsByClassName()`
*`document.getElementsByTagName()`


###Modern Selector:
*`document.querySelector()`
*`document.query.selector()`
*Difference between `NodeList`and`HTMLcollection`



## `*1,HTML collection`

## **An html collection is a live collection of html element only.

"live"means:

**its automatically update when the dom changes.

### common ways to get it

document.getElementByTagName("div")
document.getElementByClassName("box")
documents.forms
documents.images


# **key points **
`*elements only(no text,comments)*
`*live(auto-updates)*
❌ No for each() method
`*access by index or name*


2.NodeList(often called "node collection")
what it is

a nodeList is a collection of nodes which can include
`*elements`
`*text nodes`
`*comment nodes`


Feature     HTMLCollection	NodeList


Contains	Elements only	Any node

Live	    ✅ Yes	      ❌ Usually No
forEach()	❌ No	      ✅ Yes
Returned by	getElementsBy*	querySelectorAll


5. Simple Rule to Remember

`*HTMLCollection → live, elements only'*

`*NodeList → usually static, all node types`*



### ** changing content **

* `element.innerText`
*` element.textContent`
*`element.innerHtml`(and dangers of using it)
*setting vs getting content
