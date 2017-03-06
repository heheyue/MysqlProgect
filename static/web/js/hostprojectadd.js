/**
 * Created by root on 17-3-3.
 */
/**
 * Created by root on 17-2-9.
 */
var csrftoken = $.cookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

function ChoseProjectByAjax() {
    var temp=$("#ChoseProject").val();
    console.log(temp);
     $.ajax({
         url:'/web/hostprojectadd/',
         type:'POST',
         data:{ChoseProjectByAjax:temp},
         success:function (arg) {
             var obj = jQuery.parseJSON(arg);
             var music="<tr>"+"<td>"+"IP"+"</td>"+"<td>"+"HostDescription"+"</td>"+"</tr>";
             for (var i=0;i<obj.length;i++) {
                 j = obj[i];
                 music += "<tr>" + "<td>" + j["Ip"] + "</td>" + "<td>" + j["HostDescription"] + "</td>" + "</tr>";
                 // alert(j.id);
                 // alert(j.Ip);
                 //$('#HostAll').append(music);
                 // alert(music)l
             }
             document.getElementById("HostIp").innerHTML=music;
             document.getElementById("Msg").innerHTML="";
         },
         error:function () {
             console.log('error')
         }
     });
}
