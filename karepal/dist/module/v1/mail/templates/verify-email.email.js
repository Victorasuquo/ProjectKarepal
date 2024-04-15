"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.VerifyEmailTemplate = void 0;
function VerifyEmailTemplate(data) {
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
    <p>Enter this 6-digit code to verify your identity and gain access to your Karepal account. This code
      <b>expires</b>
      in 15 minutes</p>
    <h2> ${data.code}</h2>
    <p style='font-size:0.9em;'>Regards,<br />The Karepal Team</p>
    <hr style='border:none;border-top:1px solid #eee' />
    <div
      style='float:right;padding:8px 0;color:#aaa;font-size:0.8em;line-height:1;font-weight:300'
    >
      <p>karepal</p>
    </div>
  </div>
</div>`;
}
exports.VerifyEmailTemplate = VerifyEmailTemplate;
//# sourceMappingURL=verify-email.email.js.map