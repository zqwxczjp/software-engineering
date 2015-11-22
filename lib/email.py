#coding:utf-8
import uuid
import time
from django.core.mail import EmailMultiAlternatives 
#向用户发送激活邮件
def send_active_email(email):
    if isinstance(email, unicode):
        email = email.encode('utf-8')
    ActiveCode = active_code(email)
    html_content = u'<b>激活链接：</b><a href="active/%s">http://hitquanzi/active/%s</a>' % (ActiveCode, ActiveCode)
    subject, form_email, to = u'激活邮件', 'hitquanzi@sina.com', email
    text_content = u'感谢您注册工大圈子，请点击下面的'
    msg = EmailMultiAlternatives(subject, text_content, form_email, [to])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
    #return HttpResponse(u'请查看你注册的信箱完成注册!!')
    return ActiveCode

#激活码计算:邮箱+当前时间
def active_code(email):
    email_code = uuid.uuid5(uuid.NAMESPACE_DNS, email+str(time.time())).hex
    return email_code
    
print send_active_email('2546@qq.com')