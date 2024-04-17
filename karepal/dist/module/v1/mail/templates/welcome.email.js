"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.welcomeEmailTemplate = void 0;
function welcomeEmailTemplate(data) {
    return `
    <!DOCTYPE html>
<html>
<head>
  <title>Welcome Email</title>
</head>
<body>
  <h1>Welcome, ${data.name}!</h1>
  <p>Thank you for joining our platform. We are excited to have you on board.</p>
  <p>If you have any questions or need assistance, feel free to reach out to our support team.</p>
  <p>Best regards,</p>
  <p>karepal</p>
</body>
</html>
    `;
}
exports.welcomeEmailTemplate = welcomeEmailTemplate;
//# sourceMappingURL=welcome.email.js.map