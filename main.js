function div(){
    var inter = ''
    for (var i = 0; i < arguments.length; ++i)
        inter += arguments[i]
    
    
    
    return '<div>'+inter+'</div>'
}

function p(){
    var inter = ''
    for (var i = 0; i < arguments.length; ++i)
        inter += arguments[i]

    return '<p>'+inter+'</p>'
}

function button(){
    var inter = ''
    for (var i = 0; i < arguments.length; ++i)
        inter += arguments[i]

    return '<button class="waves-effect waves-light btn">'+inter+'</button>'
}

function render (html){
    var root = document.getElementById('root');
    root.innerHTML = html
}
