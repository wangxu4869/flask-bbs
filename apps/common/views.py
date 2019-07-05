from flask import Blueprint,request,make_response,jsonify
from exts import alidayu
from utils import restful,zlcache
from utils.captcha import Captcha
from .forms import SMSCaptchaForm
from io import BytesIO
import qiniu
from tasks import send_sms_captcha
# from utils import smssender

bp=Blueprint('common',__name__,url_prefix='/c')



@bp.route('/sms_captcha/',methods=['POST'])
def sms_captcha():
    #teltphone
    #timestamp
    #md5(timestamp+teltphone+salt)
    form=SMSCaptchaForm(request.form)
    if form.validate():
        telephone=form.telephone.data
        captcha=Captcha.gene_text(number=4)
        #感觉此处应该加delay老师没加
        send_sms_captcha.delay(telephone,captcha)
        # smssender.send(telephone,captcha)
        return restful.success()

    else:
        return restful.params_error(message='参数错误！')


@bp.route('/captcha/')
def graph_captcha():
    text,image=Captcha.gene_graph_captcha()
    zlcache.set(text.lower(),text.lower())
    out=BytesIO()
    image.save(out,'png')
    out.seek(0)
    resp=make_response(out.read())
    resp.content_type='image/png'
    return resp

@bp.route('/uptoken/')
def uptoken():
    access_key = '9-7_e1Ib_BMkgbdsSgmpGoW_VIrTYMGKO-3XdxtG'
    secret_key = 'FzvqhdlgxRaOw5Kh2CvmrJkce8-s-e1Aq9wl7S0h'
    q = qiniu.Auth(access_key,secret_key)

    bucket = 'wxvideo'
    token = q.upload_token(bucket)
    return jsonify({'uptoken':token})

