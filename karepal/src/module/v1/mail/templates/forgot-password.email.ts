import { ISendResetPasswordEmailTemplate } from 'src/common/interfaces/email-templates.interface';

export function ForgotPasswordTemplate(data: ISendResetPasswordEmailTemplate) {
  return `<div
  style='font-family: Helvetica,Arial,sans-serif;min-width:1000px;overflow:auto;line-height:2'
>
  <div style='margin:50px auto;width:70%;padding:20px 0'>
    <div style='border-bottom:1px solid #eee'>
      <a
        href=''
        style='font-size:1.4em;color: #00466a;text-decoration:none;font-weight:600'
      >karepal</a>
    </div>
    <p style='font-size:1.1em'>Hi,</p>
    <p>This is the code to reset your password. This code
      <b>expires</b>
      in 15 minutes</p>
    <h2
      style='background: #00466a;margin: 0 auto;width: max-content;padding: 0 10px;color: #fff;border-radius: 4px;'
    >${data.code}</h2>
    <p style='font-size:0.9em;'>Regards,<br />karepal</p>
    <hr style='border:none;border-top:1px solid #eee' />
    <div
      style='float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300'
    >
      <p>karepal</p>
    </div>
  </div>
</div>`;
}
