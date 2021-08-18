//
//  routes.swift
//  Library API
//
//  Created by Paul Schifferer on 4/22/17.
//  Copyright 2021 SweetRPG. All rights reserved.
//

import Fluent
import Vapor
import Common


func routes(_ app: Application) throws {
    try app.register(collection: VolumesController())
    try app.register(collection: HealthController<LibraryHealthInfo>(healthCallback: healthCallback))
}
