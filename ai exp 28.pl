% Facts: Diseases and their symptoms
disease(flu, [fever, cough, body_ache]).
disease(cold, [cough, sneezing, runny_nose]).
disease(covid, [fever, cough, loss_of_taste]).
disease(malaria, [fever, chills, sweating]).
disease(diabetes, [frequent_urination, excessive_thirst, weight_loss]).

% Rule to get symptoms of a disease
symptoms(Disease, Symptoms) :- disease(Disease, Symptoms).

