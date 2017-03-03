/**
 * Created by root on 17-3-1.
 */
$(document).ready(
    function() {
	    $("#DbUserAdd").validVal({
			form:{
	            onInvalid:function () {
                    alert("请补全必填字段")
                }
            }
		});
	});