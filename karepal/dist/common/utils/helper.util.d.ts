export declare class BaseHelper {
    static generateRandomString(length?: number): string;
    static hashData(data: string): Promise<string>;
    static compareHashedData(data: string, hashed: string): Promise<boolean>;
    static generateOTP(): number;
    static encryptData(data: string, encryptionKey?: string): string;
    static decryptData(encryptedData: string, encryptionKey?: string): string;
    static generateEncryptionKey(): string;
}
