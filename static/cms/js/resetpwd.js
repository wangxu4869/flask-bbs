$(function () {
    $('#submit').click(function (event) {
        event.preventDefault();

        var oldpwdE=$('input[name=oldpwd]');
        var newpwdE=$('input[name=newpwd]');
        var newpwd_repeatE=$('input[name=newpwd_repeat]');

        var oldpwd=oldpwdE.val();
        var newpwd=newpwdE.val();
        var newpwd_repeat=newpwd_repeatE.val();

        zlajax.post({
            'url':'/cms/resetpwd/',
            'data':{
                'oldpwd':oldpwd,
                'newpwd':newpwd,
                'newpwd_repeat':newpwd_repeat
            },
            'success':function (data) {
                if(data['code']==200){
                    zlalert.alertSuccessToast('恭喜！修改密码成功！');
                    oldpwdE.val('');
                    newpwdE.val('');
                    newpwd_repeatE.val('');
                }else{
                    var message=data['message'];
                    zlalert.alertInfo(message);
                }
            },
            'fail':function (error) {
                zlalert.alertNetworkError();
            }
        });
    });
});