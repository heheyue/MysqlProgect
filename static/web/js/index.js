/**
 * Created by root on 17-2-10.
 */

var pagenum = 0
var numpage = 2
function next() {
    pagenum=pagenum + 1;
    console.log(pagenum);
    $.ajax({
        url:'/index/',
        type:'POST',
        data:{'pagenum':pagenum,'numpage':numpage},
        success:function (arg) {
            $().HTML(arg);
            // console.log(arg.hostname);
         },
         error:function () {
             console.log('error')
         }
    })
}

$(function () {
    var value = $.cookie("Pagenum");
    if (value){
        $('#valueId').val(value)
    }
})

function ChangePage(arg) {
    var value = $(arg).val();
    $.cookie("Pagenum",value,{ path:'/'});
}
