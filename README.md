# PANDA

## Table of Contents

1. [Introduction](#introduction)
   - 1.1 [Purpose](#purpose)
   - 1.2 [Scope](#scope)
   - 1.3 [Target Audience](#target-audience)

2. [System Architecture](#system-architecture)
   - 2.1 [AWS Hosting](#aws-hosting)
   - 2.2 [RAG and LLMs for Questionnaire Generation](#rag-and-llms-for-questionnaire-generation)
   - 2.3 [Decision Tree Method](#decision-tree-method)
   - 2.4 [Voice Analysis](#voice-analysis)

3. [Workflow](#workflow)
   - 3.1 [User Interaction](#user-interaction)
   - 3.2 [Questionnaire Generation](#questionnaire-generation)
   - 3.3 [Decision Tree Analysis](#decision-tree-analysis)
   - 3.4 [Voice Emotion Analysis](#voice-emotion-analysis)
   - 3.5 [Conclusion Generation](#conclusion-generation)

4. [Abnormality Detection](#abnormality-detection)
   - 4.1 [List of Abnormalities](#list-of-abnormalities)
   - 4.2 [Criteria for Detection](#criteria-for-detection)
   - 4.3 [Combined Results](#combined-results)

5. [Aid and Support](#aid-and-support)
   - 5.1 [Solution Suggestions](#solution-suggestions)
   - 5.2 [User Resources](#user-resources)
   - 5.3 [Emergency Procedures](#emergency-procedures)

6. [Security and Privacy](#security-and-privacy)
   - 6.1 [Data Handling](#data-handling)
   - 6.2 [Encryption](#encryption)
   - 6.3 [Privacy Measures](#privacy-measures)

7. [User Guidelines](#user-guidelines)
   - 7.1 [Accessing the Chatbot](#accessing-the-chatbot)
   - 7.2 [Providing Accurate Information](#providing-accurate-information)
   - 7.3 [Understanding Results](#understanding-results)
   - 7.4 [Seeking Professional Help](#seeking-professional-help)

## 1. Introduction

### 1.1 Purpose
The chatbot provides a convenient platform for individuals to assess their mental health through casual conversation, aiming to detect various abnormalities.

### 1.2 Scope
Focused on detecting eight types of abnormalities: depression, PTSD, anxiety, schizophrenia, bipolar disorder, bulimia, anorexia, and OCD.

### 1.3 Target Audience
Designed for individuals seeking a preliminary assessment of their mental health who may be hesitant to approach a professional directly.

## 2. System Architecture

### 2.1 AWS Hosting
Hosted on AWS for scalability, reliability, and security, utilizing services for data storage and computational load handling.

### 2.2 RAG and LLMs for Questionnaire Generation
Utilizes Randomized Answer Generation (RAG) and Large Language Models (LLMs) for dynamic and personalized questionnaire generation.

### 2.3 Decision Tree Method
Implements a decision tree algorithm to analyze user responses and identify potential mental health abnormalities.

### 2.4 Voice Analysis
Incorporates voice analysis technology to assess the emotional tone of the user in real-time.

## 3. Workflow

### 3.1 User Interaction
Users engage in a natural conversation guided by RAG and LLMs, progressing through dynamically generated questionnaires.

### 3.2 Questionnaire Generation
Questions are dynamically generated based on user responses, adapting the conversation flow for relevant mental health information.

### 3.3 Decision Tree Analysis
User responses are processed through a decision tree algorithm, refining predictions with each input.

### 3.4 Voice Emotion Analysis
Real-time voice analysis enhances understanding of the user's emotional state.

### 3.5 Conclusion Generation
Combines results from decision tree and voice emotion analysis to generate a conclusion regarding potential mental health abnormalities.

## 4. Abnormality Detection

### 4.1 List of Abnormalities
- Depression
- PTSD
- Anxiety
- Schizophrenia
- Bipolar Disorder
- Bulimia
- Anorexia
- OCD

### 4.2 Criteria for Detection
Each abnormality is associated with specific criteria within the decision tree, matched to user responses.

### 4.3 Combined Results
The final conclusion is drawn by considering both decision tree and voice emotion analysis.

## 5. Aid and Support

### 5.1 Solution Suggestions
Tailored suggestions provided based on detected abnormalities, including self-help strategies and encouragement to seek professional help.

### 5.2 User Resources
Users are provided with relevant mental health resources, such as helplines and support groups.

### 5.3 Emergency Procedures
In cases of severe distress, the chatbot guides users on emergency procedures and strongly encourages seeking immediate professional assistance.

## 6. Security and Privacy

### 6.1 Data Handling
User data is handled with confidentiality, securely stored and processed.

### 6.2 Encryption
Communication is encrypted to protect sensitive information during transmission.

### 6.3 Privacy Measures
Includes privacy features, allowing users to delete conversation history and providing clear information about data storage and usage practices.

## 7. User Guidelines

### 7.1 Accessing the Chatbot
Users can access the chatbot through a user-friendly interface for a seamless experience.

### 7.2 Providing Accurate Information
Users are encouraged to provide accurate responses for an accurate mental health assessment.

### 7.3 Understanding Results
Clear and understandable explanations of conclusions are provided, emphasizing the preliminary nature of the assessment.

### 7.4 Seeking Professional Help
The chatbot emphasizes the importance of consulting with a mental health professional for a more comprehensive evaluation.

Users are encouraged to provide feedback to enhance the user experience.

### 8.3 Bug Reporting
A dedicated bug reporting system is in place to address technical issues promptly.
