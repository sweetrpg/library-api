//
//  migrations.swift
//  Library API
//
//  Created by Paul Schifferer on 4/22/17.
//  Copyright 2021 SweetRPG. All rights reserved.
//

import Vapor
import Fluent


public func migrations(_ app : Application) throws {
    // app.migrations.add(SeedDatabase())

    switch app.environment {
    case .development, .testing:
        // TODO: non-production migrations
        break
    default:
        break
    }

    app.migrations.add(CacheEntry.migration)

    app.logger.logLevel = .debug
    try app.autoMigrate().wait()
}
