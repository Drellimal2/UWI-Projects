window.onload = function(){
    $("lookup").onclick = function(){
        var search = $("term").value;
        //alert(search);
        new Ajax.Updater("result","http://lab8-c9-drellimal2.c9.io/world.php?lookup="+search,
        {
            method: "get"

        }
        );
    }

};

function handleRequest(ajax) {
};