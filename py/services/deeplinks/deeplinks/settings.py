import environs

ENV = environs.Env()
ENV.read_env(".env")

IP_ADDRESS_META_FIELD = ENV("IP_ADDRESS_META_FIELD", default="X-Forwarded-For")

DEEPLINK_SECRET_KEY = ENV("DEEPLINK_SECRET_KEY", default="90fce962aa905e94c22c97efbe7326d2")
