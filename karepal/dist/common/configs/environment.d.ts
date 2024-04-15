export interface IEnvironment {
    APP: {
        NAME: string;
        PORT: number | string;
        ENV: string;
        ENCRYPTION_KEY: string;
    };
    DB: {
        URL: string;
    };
    JWT: {
        SECRET: string;
    };
    MAILER: {
        SMTP: string;
        HOST: string;
        PORT: string;
        EMAIL: string;
        PASSWORD: string;
    };
    AWS: {
        ACCOUNT_ID: string;
        REGION: string;
        ACCESS_KEY: string;
        SECRET: string;
        BUCKET_NAME: string;
        BUCKET_URL: string;
    };
    REDIS: {
        URL: string;
    };
}
export declare const ENVIRONMENT: IEnvironment;
