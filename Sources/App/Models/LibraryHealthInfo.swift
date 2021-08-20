//
//  LibraryHealthInfo.swift
//  Library API
//
//  Created by Paul Schifferer on 4/22/17.
//  Copyright 2021 SweetRPG. All rights reserved.
//

import Vapor
import Common


/**
 */
struct LibraryHealthInfo : HealthInfo, Content {
/**
The timestamp of the health response.
 */
    let timestamp : Date
/**
 */
    let dbHealthy : Bool
}

/**
 */
func healthCallback() -> LibraryHealthInfo {
    return LibraryHealthInfo(timestamp: Date(), dbHealthy: true)
}
