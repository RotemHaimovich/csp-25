#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>

// Word lists
const char *nouns[] = {"chair", "clock", "dog", "cat", "pizza", "computer", "blanket", "hand"};
const char *verbs[] = {"yaps", "naps", "thinks", "runs", "eats", "sleeps", "dreams", "flies"};
const char *adjectives[] = {"silly", "little", "tall", "unc", "wise", "tired", "happy", "quick"};
const char *adverbs[] = {"sadly", "quickly", "sleepily", "loudly", "carefully", "happily", "slowly"};
const char *determiners[] = {"the", "a", "my", "our", "his", "her", "your", "their"};
const char *prepositions[] = {"near", "over", "under", "beside", "through", "around", "above"};
const char *names[] = {"Siddhi", "Rotem", "Idan", "Bridger", "Varenya", "Finn", "Akash"};

#define ARRAY_SIZE(arr) (sizeof(arr) / sizeof(arr[0]))
#define MAX_PHRASE_LEN 200

// Random word reporters
const char* random_noun() {
    return nouns[rand() % ARRAY_SIZE(nouns)];
}

const char* random_verb() {
    return verbs[rand() % ARRAY_SIZE(verbs)];
}

const char* random_adjective() {
    return adjectives[rand() % ARRAY_SIZE(adjectives)];
}

const char* random_adverb() {
    return adverbs[rand() % ARRAY_SIZE(adverbs)];
}

const char* random_determiner() {
    return determiners[rand() % ARRAY_SIZE(determiners)];
}

const char* random_preposition() {
    return prepositions[rand() % ARRAY_SIZE(prepositions)];
}

const char* random_name() {
    return names[rand() % ARRAY_SIZE(names)];
}

// Simple sentence reporter
void simple_sentence(char *result) {
    sprintf(result, "%s %s %s", random_determiner(), random_noun(), random_verb());
}

// Noun phrase reporter 
void noun_phrase(char *result) {
    int use_name = rand() % 5 == 0; // 20% chance to use a name
    
    if (use_name) {
        strcpy(result, random_name());
    } else {
        int adj_count = rand() % 3; // 0, 1, or 2 adjectives
        
        if (adj_count == 0) {
            sprintf(result, "%s %s", random_determiner(), random_noun());
        } else if (adj_count == 1) {
            sprintf(result, "%s %s %s", random_determiner(), random_adjective(), random_noun());
        } else {
            sprintf(result, "%s %s %s %s", random_determiner(), random_adjective(), 
                    random_adjective(), random_noun());
        }
    }
}

// Prepositional phrase reporter
void prepositional_phrase(char *result) {
    char np[MAX_PHRASE_LEN];
    noun_phrase(np);
    sprintf(result, "%s %s", random_preposition(), np);
}

// Verb phrase reporter
void verb_phrase(char *result) {
    if (rand() % 2 == 0) {
        strcpy(result, random_verb());
    } else {
        sprintf(result, "%s %s", random_verb(), random_adverb());
    }
}

// Complicated sentence reporter
void complicated_sentence(char *result) {
    char np[MAX_PHRASE_LEN];
    char vp[MAX_PHRASE_LEN];
    char pp[MAX_PHRASE_LEN];
    
    noun_phrase(np);
    verb_phrase(vp);
    prepositional_phrase(pp);
    
    sprintf(result, "%s %s %s", np, vp, pp);
}

int main() {
    char sentence[MAX_PHRASE_LEN];
    
    // Seed random number generator
    srand(time(NULL));
    
    printf("=== Sentence Builder ===\n\n");
    
    // Test simple sentences
    printf("Simple sentences:\n");
    for (int i = 0; i < 5; i++) {
        simple_sentence(sentence);
        printf("  %s.\n", sentence);
    }
    
    printf("\n");
    
    // Test complicated sentences
    printf("Complicated sentences:\n");
    for (int i = 0; i < 10; i++) {
        complicated_sentence(sentence);
        printf("  %s.\n", sentence);
    }
    
    printf("\n");
    
    // Test individual phrases
    printf("Sample noun phrases:\n");
    for (int i = 0; i < 5; i++) {
        noun_phrase(sentence);
        printf("  %s\n", sentence);
    }
    
    printf("\nSample verb phrases:\n");
    for (int i = 0; i < 5; i++) {
        verb_phrase(sentence);
        printf("  %s\n", sentence);
    }
    
    printf("\nSample prepositional phrases:\n");
    for (int i = 0; i < 5; i++) {
        prepositional_phrase(sentence);
        printf("  %s\n", sentence);
    }
    
    return 0;
}