import os
import json

def path_to_dict(path):
    d = {'name': os.path.basename(path)}
    if os.path.isdir(path):
        d['type'] = "directory"
        d['children'] = [path_to_dict(os.path.join(path,x)) for x in os.listdir\
(path)]
    else:
        d['type'] = "file"
    return d

f = open("./src/home.js", "a", encoding="utf-8")
f.truncate(0)
f.write("var dir_tree = ")
json.dump(path_to_dict('./courses/'), f, ensure_ascii=False, indent=4)
f.write("\r\nvar index = null;\r\n\r\nvar moduleTitle = null;\r\n\r\nvar moduleIndex;\r\n\r\nwindow.onload = function () {\r\n\r\n    var url = document.location.href,\r\n\r\n        params = url.split('?')[1].split('&'),\r\n\r\n        data = {}, tmp;\r\n\r\n    for (var i = 0, l = params.length; i < l; i++) {\r\n\r\n        tmp = params[i].split('=');\r\n\r\n        data[tmp[0]] = tmp[1];\r\n\r\n    }\r\n\r\n    title = data.name.split(\"%20\").join(\" \");\r\n\r\n    this.moduleTitle = title.split(\"%23\")[0];\r\n\r\n    this.index = title.split(\"%23\")[1];\r\n\r\n    document.getElementById('title').innerHTML = this.moduleTitle;\r\n\r\n    console.log(\"Index :\" + this.index);\r\n\r\n\r\n\r\n    getMedia();\r\n\r\n\r\n\r\n\r\n\r\n}\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\nfunction getMedia() {\r\n\r\n\r\n\r\n    var module = dir_tree['children'][index]['children'];\r\n\r\n\r\n\r\n    moduleIndex = dir_tree['children'][index]['children'].findIndex(function (person) {\r\n\r\n\r\n\r\n        return person.name == moduleTitle;\r\n\r\n    });\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n    var mediaTree = module[moduleIndex]['children'];\r\n\r\n\r\n\r\n    var mediaEle = document.getElementById(\"mediaList\");\r\n\r\n\r\n\r\n    var rawMedia = [];\r\n\r\n    for (i = 0; i < mediaTree.length; i++) {\r\n\r\n\r\n\r\n        media = mediaTree[i].name;\r\n\r\n        if (mediaTree[i].type == \"file\") {\r\n\r\n\r\n\r\n            check = media.slice(-4);\r\n\r\n\r\n\r\n            if (check == \".mp4\") {\r\n\r\n\r\n\r\n\r\n\r\n                rawMedia.push(media);\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n            }\r\n\r\n\r\n\r\n        }\r\n\r\n    }\r\n\r\n\r\n\r\n    rawMedia.sort((a, b) => a.split(\".\")[0] - b.split(\".\")[0]);\r\n\r\n    for (i = 0; i < rawMedia.length; i++) {\r\n\r\n        var node = document.createElement(\"LI\");\r\n\r\n        node.className = \"mediali\";\r\n\r\n        node.className = \"list-group-item\";\r\n\r\n        var textnode = document.createTextNode(rawMedia[i].slice(0, -4));\r\n\r\n        node.appendChild(textnode);\r\n\r\n        mediaEle.append(node)\r\n\r\n    }\r\n\r\n\r\n\r\n\r\n\r\n}\r\n\r\n\r\n\r\n\r\n\r\nvar ul = document.getElementById('mediaList');\r\n\r\nvar heaEle = document.getElementById('mediaTitle');\r\n\r\n\r\n\r\nul.onclick = function (event) {\r\n\r\n\r\n\r\n    var name = event.target.innerHTML;\r\n\r\n    heaEle.innerHTML = name;\r\n\r\n    var mediaPlayer = document.getElementById('mediaPlayer');\r\n\r\n    var media_src = \"courses\\\\\/\" + dir_tree['children'][index].name + \"\\\\\/\" + dir_tree['children'][index]['children'][moduleIndex].name + \"\\\\\/\" + name + \".mp4\";\r\n\r\n    console.log(media_src);\r\n\r\n    mediaPlayer.src = media_src;\r\n\r\n};\r\n")
f.close()

f = open("./src/script.js", "a", encoding="utf-8")
f.truncate(0)
f.write("var dir_tree = ")
json.dump(path_to_dict('./courses/'), f, ensure_ascii=False, indent=4)
f.write("\r\ngetCourseName(dir_tree);\r\n\r\n\r\n\r\nvar index=null;\r\n\r\n\r\n\r\nfunction getCourseName(main_dir) {\r\n\r\n\r\n\r\n\r\n\r\n    var total_course = dir_tree['children'].length;\r\n\r\n\r\n\r\n    for (i = 0; i < parseInt(total_course); i++) {\r\n\r\n\r\n\r\n        if (dir_tree['children'][i].type == \"directory\") {\r\n\r\n\r\n\r\n\r\n\r\n            var node = document.createElement(\"LI\");\r\n\r\n            node.className = \"list-group-item\";\r\n\r\n            var textnode = document.createTextNode(dir_tree['children'][i].name);\r\n\r\n            node.appendChild(textnode);\r\n\r\n\r\n\r\n            var main = document.getElementById(\"courseList\");\r\n\r\n            main.append(node);\r\n\r\n        }\r\n\r\n\r\n\r\n\r\n\r\n    }\r\n\r\n\r\n\r\n}\r\n\r\n\r\n\r\nvar ul = document.getElementById('courseList');\r\n\r\nul.onclick = function (event) {\r\n\r\n\r\n\r\n\r\n\r\n    var name = event.target.innerHTML;\r\n\r\n\r\n\r\n    var titleEle = document.getElementById(\"title\");\r\n\r\n    titleEle.innerHTML = name;\r\n\r\n\r\n\r\n    var courseContainer = document.getElementById(\"courseContainer\");\r\n\r\n    courseContainer.hidden = true;\r\n\r\n\r\n\r\n    var module = document.getElementById(\"module\");\r\n\r\n    module.hidden = false;\r\n\r\n\r\n\r\n    var backButton = document.getElementById(\"backButton\");\r\n\r\n    backButton.hidden = false;\r\n\r\n\r\n    name = name.split(\"&amp;\").join(\"&\");\r\n\r\n    getModuleList(name);\r\n\r\n\r\n\r\n};\r\n\r\n\r\n\r\nfunction backButton() {\r\n\r\n\r\n\r\n    var titleEle = document.getElementById(\"title\");\r\n\r\n    titleEle.innerHTML = \"My Courses\";\r\n\r\n    var courseContainer = document.getElementById(\"courseContainer\");\r\n\r\n    courseContainer.hidden = false;\r\n\r\n\r\n\r\n    var module = document.getElementById(\"module\");\r\n\r\n    module.hidden = true;\r\n\r\n    var backButton = document.getElementById(\"backButton\");\r\n\r\n    backButton.hidden = true;\r\n\r\n\r\n\r\n    var moduleList = document.getElementById(\"moduleList\");\r\n\r\n\r\n\r\n    moduleList.innerHTML = '';\r\n\r\n\r\n\r\n    index=null;\r\n\r\n}\r\n\r\n\r\n\r\nfunction getModuleList(courseName) {\r\n\r\n\r\n\r\n    var moduleIndex = dir_tree['children'].findIndex(function (person) {\r\n\r\n\r\n\r\n        return person.name == courseName;\r\n\r\n    });\r\n\r\n\r\n\r\n    index = moduleIndex;\r\n\r\n\r\n\r\n    var moduleTree = dir_tree['children'][moduleIndex]['children'];\r\n\r\n\r\n\r\n\r\n\r\n    var moduleList = document.getElementById(\"moduleList\");\r\n\r\n\r\n\r\n    var rawList = [];\r\n\r\n\r\n\r\n    for (i = 0; i < parseInt(moduleTree.length); i++) {\r\n\r\n        var name = moduleTree[i].name;\r\n\r\n\r\n\r\n        if (moduleTree[i].type == \"directory\") {\r\n\r\n            rawList.push(name);\r\n\r\n        }\r\n\r\n    }\r\n\r\n\r\n\r\n    rawList.sort((a, b) => a.split(\".\")[0] - b.split(\".\")[0]);\r\n\r\n\r\n\r\n    for (i = 0; i < rawList.length; i++) {\r\n\r\n\r\n\r\n        var node = document.createElement(\"LI\");\r\n\r\n        node.className = \"list-group-item\";\r\n\r\n        var textnode = document.createTextNode(rawList[i]);\r\n\r\n        node.appendChild(textnode);\r\n\r\n\r\n\r\n        moduleList.append(node);\r\n\r\n    }\r\n\r\n\r\n\r\n\r\n\r\n}\r\n\r\n\r\n\r\n\r\n\r\nvar moduleEle = document.getElementById(\"moduleList\");\r\n\r\nmoduleEle.onclick = function (event) {\r\n\r\n\r\n\r\n\r\n\r\n    var name = event.target.innerHTML;\r\n\r\n\r\n\r\n    var currentLocation = window.location.toString().slice(0, -10);\r\n\r\n    var url = currentLocation + \"home.html?name=\" + encodeURIComponent(name+\"#\"+index);\r\n\r\n\r\n\r\n\r\n\r\n    window.location.href = url;\r\n\r\n\r\n\r\n};\r\n\r\n\r\n")
f.close()

my_dict = path_to_dict('./courses/')

child = my_dict['children']
