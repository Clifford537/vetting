from rest_framework import serializers
from django.contrib.auth.models import User  # Ensure to import the User model
from .models import Client, Experience, Skill, ServiceProvider


class SkillSerializer(serializers.ModelSerializer):
    endorsedBy = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True, required=False)

    class Meta:
        model = Skill
        fields = '__all__'

    def create(self, validated_data):
        endorsed_by_data = validated_data.pop('endorsedBy', [])
        skill = Skill.objects.create(**validated_data)
        skill.endorsedBy.set(endorsed_by_data)
        return skill

    def update(self, instance, validated_data):
        endorsed_by_data = validated_data.pop('endorsedBy', [])
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        instance.endorsedBy.set(endorsed_by_data)
        return instance


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'


class ServiceProviderSerializer(serializers.ModelSerializer):
    skill = SkillSerializer(many=True)  # To handle nested skill creation
    experience = ExperienceSerializer(many=True)  # To handle nested experience creation

    class Meta:
        model = ServiceProvider
        fields = ['location', 'skill', 'experience', 'portfolio']

    def create(self, validated_data):
        skills_data = validated_data.pop('skill')
        experiences_data = validated_data.pop('experience')

        service_provider = ServiceProvider.objects.create(**validated_data)

        for skill_data in skills_data:
            skill, created = Skill.objects.get_or_create(**skill_data)
            service_provider.skill.add(skill)

        for experience_data in experiences_data:
            experience, created = Experience.objects.get_or_create(**experience_data)
            service_provider.experience.add(experience)

        return service_provider
    skill = SkillSerializer(many=True)
    experience = ExperienceSerializer(many=True)

    class Meta:
        model = ServiceProvider
        fields = ['location', 'skill', 'experience', 'portfolio']

    def create(self, validated_data):
        skills_data = validated_data.pop('skill', [])
        experiences_data = validated_data.pop('experience', [])

        service_provider = ServiceProvider.objects.create(**validated_data)

        for skill_data in skills_data:
            skill, created = Skill.objects.update_or_create(
                user=skill_data.get('user'),
                skillName=skill_data.get('skillName'),
                proficiencyLevel=skill_data.get('proficiencyLevel'),
                defaults=skill_data
            )
            service_provider.skill.add(skill)

        for experience_data in experiences_data:
            experience, created = Experience.objects.update_or_create(
                user=experience_data.get('user'),
                jobTitle=experience_data.get('jobTitle'),
                company=experience_data.get('company'),
                startDate=experience_data.get('startDate'),
                defaults=experience_data
            )
            service_provider.experience.add(experience)

        return service_provider

    def update(self, instance, validated_data):
        skills_data = validated_data.pop('skill', [])
        experiences_data = validated_data.pop('experience', [])

       
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        instance.skill.clear()
        for skill_data in skills_data:
            skill, created = Skill.objects.update_or_create(
                user=skill_data.get('user'),
                skillName=skill_data.get('skillName'),
                proficiencyLevel=skill_data.get('proficiencyLevel'),
                defaults=skill_data
            )
            instance.skill.add(skill)

   
        instance.experience.clear()
        for experience_data in experiences_data:
            experience, created = Experience.objects.update_or_create(
                user=experience_data.get('user'),
                jobTitle=experience_data.get('jobTitle'),
                company=experience_data.get('company'),
                startDate=experience_data.get('startDate'),
                defaults=experience_data
            )
            instance.experience.add(experience)

        return instance



class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


        
