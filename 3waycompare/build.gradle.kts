plugins {
    id("java")
    id("application")
}

group = "com.scoop.competitive"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

java {
    sourceCompatibility = JavaVersion.VERSION_17
    targetCompatibility = JavaVersion.VERSION_17
}

application {
    mainClass.set("com.scoop.competitive.AIComparisonApp")
}

dependencies {
    // Scoop project dependencies
    implementation(files("../../scoop/app/build/libs/app.jar"))

    // Markdown parsing
    implementation("com.vladsch.flexmark:flexmark-all:0.64.8")

    // YAML parsing for frontmatter and config
    implementation("com.fasterxml.jackson.dataformat:jackson-dataformat-yaml:2.15.2")
    implementation("com.fasterxml.jackson.core:jackson-databind:2.15.2")
    implementation("com.fasterxml.jackson.datatype:jackson-datatype-jsr310:2.15.2")

    // File I/O utilities
    implementation("commons-io:commons-io:2.13.0")

    // Template engine (Mustache for template filling)
    implementation("com.github.spullara.mustache.java:compiler:0.9.11")

    // Logging
    implementation("org.slf4j:slf4j-api:2.0.9")
    implementation("ch.qos.logback:logback-classic:1.4.11")

    // JSON processing
    implementation("com.google.code.gson:gson:2.10.1")

    // Configuration (needed by Scoop)
    implementation("org.cfg4j:cfg4j-core:4.4.1")
    implementation("org.cfg4j:cfg4j-git:4.4.1")  // For git-based config if needed

    // AWS SDK v1 (needed by ScoopMetadata - must match Scoop's version)
    implementation(platform("com.amazonaws:aws-java-sdk-bom:1.12.607"))
    implementation("com.amazonaws:aws-java-sdk-s3")
    implementation("com.amazonaws:aws-java-sdk-dynamodb")
    implementation("com.amazonaws:aws-java-sdk-secretsmanager")

    // AWS SDK v2 (also needed by Scoop)
    implementation(platform("software.amazon.awssdk:bom:2.26.30"))
    implementation("software.amazon.awssdk:s3")
    implementation("software.amazon.awssdk:s3-transfer-manager")
    implementation("software.amazon.awssdk:dynamodb-enhanced")
    implementation("software.amazon.awssdk:lambda")
    implementation("software.amazon.awssdk:sesv2")
    implementation("software.amazon.awssdk:apigatewaymanagementapi")
    implementation("software.amazon.awssdk:bedrockruntime")
    implementation("software.amazon.awssdk:cognitoidentityprovider")

    // Database drivers (needed by ScoopMetadata)
    implementation("org.mariadb.jdbc:mariadb-java-client:3.1.4")

    // Testing
    testImplementation(platform("org.junit:junit-bom:5.10.0"))
    testImplementation("org.junit.jupiter:junit-jupiter")
    testImplementation("org.assertj:assertj-core:3.24.2")
}

tasks.test {
    useJUnitPlatform()
}

tasks.named<JavaExec>("run") {
    // Pass system properties for paths
    systemProperty("competitive.intelligence.path", "../competitive-intelligence")
    systemProperty("webflow.output.path", "../webflow-competitive-intelligence")
    systemProperty("scoop.path", "../scoop")
}