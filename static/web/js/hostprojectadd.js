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

console.log($('#ChoseProject'));
function ChoseProjectByAjax() {
    // alert('sadkjsdkajdlksajd')
    console.log($('#ChoseProject'));
    var temp = $('#ChoseProject').val();
    console.log(temp);
     $.ajax({
         url:'/web/hostprojectadd/',
         type:'POST',
         data:{dat:temp},
         success:function (arg) {
             var obj = jQuery.parseJSON(arg);
             console.log(obj)
             for i in obj:
                    console.log()
            //  console.log(obj.data);
            // // $('#HostAll').val(obj.data)
            //  console.log(arg);
         },
         error:function () {
             console.log('error')
         }
     });
}
