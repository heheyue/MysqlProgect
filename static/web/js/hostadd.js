/**
 * Created by root on 17-2-27.
 */
function CheckIP()
{  var ip = document.getElementById('HostIp').value;
   var re=/^(\d+)\.(\d+)\.(\d+)\.(\d+)$/;
   if(re.test(ip))
   {
       if( RegExp.$1<256 && RegExp.$2<256 && RegExp.$3<256 && RegExp.$4<256)
       return true;
   }
   alert("IP输入错误");
   return false;
}