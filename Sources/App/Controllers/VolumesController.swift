//
//  VolumesController.swift
//  Library API
//
//  Created by Paul Schifferer on 4/22/17.
//  Copyright 2021 SweetRPG. All rights reserved.
//

import Fluent
import Vapor
import LibraryModel


struct VolumesController : RouteCollection {
    func boot(routes : RoutesBuilder) throws {
        let volumesRoutes = routes.grouped("volumes")
//        let sessionRoutes = routes.grouped(User.sessionAuthenticator())
//        let authRoutes = sessionRoutes.grouped("auth")
//        authRoutes.get("login", use: loginHandler)
//        // authSessionRoutes.get("login", "auth0", use: loginAuth0Handler)

////        let credentialsAuthRoutes = authSessionRoutes.grouped(User.credentialsAuthenticator())
////        credentialsAuthRoutes.post("auth", "login", use: loginPostHandler)
//
//        authRoutes.post("logout", use: logoutHandler)
////        authSessionRoutes.get("auth", "register", use: registerHandler)
////        authSessionRoutes.post("auth", "register", use: registerPostHandler)
////        authSessionRoutes.get("auth", "password", "forgot", use: forgottenPasswordHandler)
////        authSessionRoutes.post("auth", "password", "reset", use: forgottenPasswordPostHandler)
////        authSessionRoutes.get("resetPassword", use: resetPasswordHandler)

//        sessionRoutes.get(use: indexHandler)
////        authSessionRoutes.get("acronyms", ":acronymId", use: acronymHandler)
////        authSessionRoutes.get("users", ":userId", use: userHandler)
////        authSessionRoutes.get("users", use: allUsersHandler)
////        authSessionRoutes.get("categories", use: allCategoriesHandler)
////        authSessionRoutes.get("categories", ":categoryId", use: categoryHandler)

        volumesRoutes.get(use: allVolumesHandler)
        volumesRoutes.get(":volumeId", use: volumeHandler)
    }

    func allVolumesHandler(_ req : Request) throws -> EventLoopFuture<[Volume]> {
        return req.eventLoop.future([])
    }

    func volumeHandler(_ req : Request) throws -> EventLoopFuture<Volume> {
        // TODO: query for slug, not ID
        throw Abort(.notFound)
    }
}
