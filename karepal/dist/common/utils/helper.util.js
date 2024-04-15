"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.BaseHelper = void 0;
const crypto_1 = require("crypto");
const bcrypt = require("bcrypt");
const environment_1 = require("../configs/environment");
const encryptionKeyFromEnv = environment_1.ENVIRONMENT.APP.ENCRYPTION_KEY;
class BaseHelper {
    static generateRandomString(length = 8) {
        return (0, crypto_1.randomBytes)(length).toString('hex');
    }
    static async hashData(data) {
        return await bcrypt.hash(data, 12);
    }
    static async compareHashedData(data, hashed) {
        return await bcrypt.compare(data, hashed);
    }
    static generateOTP() {
        return Math.floor(Math.random() * (999999 - 100000 + 1)) + 100000;
    }
    static encryptData(data, encryptionKey = encryptionKeyFromEnv) {
        const iv = (0, crypto_1.randomBytes)(16);
        const cipher = (0, crypto_1.createCipheriv)('aes-256-cbc', Buffer.from(encryptionKey), iv);
        let encryptedData = cipher.update(data, 'utf8', 'hex');
        encryptedData += cipher.final('hex');
        return iv.toString('hex') + ':' + encryptedData;
    }
    static decryptData(encryptedData, encryptionKey = encryptionKeyFromEnv) {
        const parts = encryptedData.split(':');
        const iv = Buffer.from(parts.shift(), 'hex');
        const encryptedText = parts.join(':');
        const decipher = (0, crypto_1.createDecipheriv)('aes-256-cbc', Buffer.from(encryptionKey), iv);
        let decryptedData = decipher.update(encryptedText, 'hex', 'utf8');
        decryptedData += decipher.final('utf8');
        return decryptedData;
    }
    static generateEncryptionKey() {
        const keyBytes = (0, crypto_1.randomBytes)(16);
        const encryptionKey = keyBytes.toString('hex');
        return encryptionKey;
    }
}
exports.BaseHelper = BaseHelper;
//# sourceMappingURL=helper.util.js.map