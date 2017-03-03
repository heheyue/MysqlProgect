/**
 * Created by root on 17-3-2.
 */
/**
 * Created by root on 17-3-1.
 */
$(document).ready(
    function() {
	    $("#ProjectAdd").validVal({
			form:{
	            onInvalid:function () {
                    alert("请补全必填字段")
                }
            }
		});
	});