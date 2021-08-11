//
// routes.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor
import Common


func routes(_ app: Application) throws {
    try app.register(collection: HealthController { () -> BasicHealthInfo in
        let bhi = BasicHealthInfo()
        print("health check", bhi)
        return bhi
    })
}
