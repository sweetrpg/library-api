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
import Common


struct VolumesController : RouteCollection {

    @Injected(.volumeService)
    private var volumeService : VolumeService

    func boot(routes : RoutesBuilder) throws {
        let volumesRoutes = routes.grouped("volumes")

//        let sessionRoutes = routes.grouped(User.sessionAuthenticator())
//        let authRoutes = sessionRoutes.grouped("auth")
//        authRoutes.get("login", use: loginHandler)
//        // authSessionRoutes.get("login", "auth0", use: loginAuth0Handler)

////        let credentialsAuthRoutes = authSessionRoutes.grouped(User.credentialsAuthenticator())
////        credentialsAuthRoutes.post("auth", "login", use: loginPostHandler)

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
        volumesRoutes.put(":volumeId", use: updateVolumeHandler)
        volumesRoutes.post(use: addVolumeHandler)
        volumesRoutes.delete(":volumeId", use: deleteVolumeHandler)
    }

    func allVolumesHandler(_ req : Request) throws -> EventLoopFuture<[Volume]> {
        return Volume.query(on: req.db).all()
    }

    func volumeHandler(_ req : Request) throws -> EventLoopFuture<Volume> {
        let volumeSlug = req.parameters.get("volumeId")
        return Volume.query(on: req.db)
        .filter(\.$slug ==  volumeSlug)
    }

    func updateVolumeHandler(_ req : Request) throws -> EventLoopFuture<Volume> {
        let volumeUpdate = try req.content.decode(Volume.self)
        return Volume.find("", on: req.db)
        .unwrap(or: Abort(.notFound))
        .flatMap { volume in
            volume.name = volumeUpdate.name
            volume.system = volumeUpdate.system
        }
    }

    func addVolumeHandler(_ req : Request) throws -> EventLoopFuture<Volume> {
        let volume = try req.content.decode(Volume.self)
        return volume.save(on: req.db).map { volume }
    }

    func deleteVolumeHandler(_ req : Request) throws -> EventLoopFuture<Volume> {
        // TODO: query for slug, not ID
        throw Abort(.notFound)
    }
}
