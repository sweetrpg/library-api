//
//  configure.swift
//  Library API
//
//  Created by Paul Schifferer on 4/22/17.
//  Copyright 2021 SweetRPG. All rights reserved.
//

import Fluent
import FluentMongoDriver
import Vapor
import Redis
import Common


public func configure(_ app : Application) throws {
    app.middleware.use(app.sessions.middleware)
    app.middleware.use(LogRequestMiddleware())

    guard let dbUrl = Environment.get("DATABASE_URL") else {
        fatalError("DATABASE_URL is not set in environment")
    }
    print(dbUrl)
    app.logger.debug("DATABASE_URL: \(dbUrl)")
    try app.databases.use(.mongo(connectionString: dbUrl), as: .mongo)

    let redisHostname = Environment.get("REDIS_HOSTNAME") ?? "localhost"
    let redisConfig = try RedisConfiguration(hostname: redisHostname)
    app.redis.configuration = redisConfig

    try migrations(app)

    app.sessions.use(.redis)
    app.caches.use(.fluent)

    // register routes
    try routes(app)
}
