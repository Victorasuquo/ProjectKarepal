export declare class CacheHelper {
    private redis;
    constructor();
    setCache: (key: string, value: string | object, expiry: number) => Promise<void>;
    getCache: (key: string) => Promise<any>;
    removeFromCache: (key: string) => Promise<number>;
}
