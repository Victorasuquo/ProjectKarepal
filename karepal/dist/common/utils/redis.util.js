"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.CacheHelper = void 0;
const ioredis_1 = require("ioredis");
const environment_1 = require("../configs/environment");
class CacheHelper {
    constructor() {
        this.setCache = async (key, value, expiry) => {
            const json = JSON.stringify(value);
            await this.redis.set(key, json, 'EX', expiry);
        };
        this.getCache = async (key) => {
            const json = await this.redis.get(key);
            if (json)
                return JSON.parse(json);
            return null;
        };
        this.removeFromCache = async (key) => {
            if (!key) {
                throw new Error('Invalid key provided');
            }
            const data = await this.redis.del(key);
            if (!data) {
                return null;
            }
            return data;
        };
        this.redis = new ioredis_1.default(environment_1.ENVIRONMENT.REDIS.URL);
    }
}
exports.CacheHelper = CacheHelper;
//# sourceMappingURL=redis.util.js.map