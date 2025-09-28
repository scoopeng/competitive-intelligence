package com.scoop.competitive.ai;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

/**
 * Loads and processes prompt templates from resources.
 * Handles variable substitution using {variable} syntax.
 */
public class PromptTemplateLoader {
    private static final Logger logger = LoggerFactory.getLogger(PromptTemplateLoader.class);
    private static final Pattern VARIABLE_PATTERN = Pattern.compile("\\{([^}]+)\\}");
    
    /**
     * Load a template from the resources/prompts directory.
     */
    public String loadTemplate(String templateName) throws IOException {
        String path = "/prompts/" + templateName;
        
        try (InputStream is = getClass().getResourceAsStream(path)) {
            if (is == null) {
                throw new IOException("Template not found: " + path);
            }
            
            byte[] bytes = is.readAllBytes();
            String template = new String(bytes, StandardCharsets.UTF_8);
            
            logger.debug("Loaded template: {} ({} chars)", templateName, template.length());
            return template;
        }
    }
    
    /**
     * Fill a template with context variables.
     * Replaces {variable} with values from the context map.
     */
    public String fillTemplate(String template, Map<String, Object> context) {
        StringBuffer result = new StringBuffer();
        Matcher matcher = VARIABLE_PATTERN.matcher(template);
        
        while (matcher.find()) {
            String variable = matcher.group(1);
            Object value = context.get(variable);
            
            if (value == null) {
                logger.warn("Variable not found in context: {}", variable);
                value = "{" + variable + "}"; // Keep original placeholder
            }
            
            // Escape special regex characters in replacement
            String replacement = Matcher.quoteReplacement(value.toString());
            matcher.appendReplacement(result, replacement);
        }
        matcher.appendTail(result);
        
        return result.toString();
    }
    
    /**
     * Load and fill a template in one operation.
     */
    public String loadAndFillTemplate(String templateName, Map<String, Object> context) 
            throws IOException {
        String template = loadTemplate(templateName);
        return fillTemplate(template, context);
    }
    
    /**
     * Validate that all required variables are present in context.
     */
    public boolean validateContext(String template, Map<String, Object> context) {
        Matcher matcher = VARIABLE_PATTERN.matcher(template);
        boolean valid = true;
        
        while (matcher.find()) {
            String variable = matcher.group(1);
            if (!context.containsKey(variable)) {
                logger.error("Missing required variable: {}", variable);
                valid = false;
            }
        }
        
        return valid;
    }
    
    /**
     * Extract all variable names from a template.
     */
    public java.util.Set<String> extractVariables(String template) {
        java.util.Set<String> variables = new java.util.HashSet<>();
        Matcher matcher = VARIABLE_PATTERN.matcher(template);
        
        while (matcher.find()) {
            variables.add(matcher.group(1));
        }
        
        return variables;
    }
}