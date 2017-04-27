from django import forms
# from .models import Song

class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = ['genre', 'subj', 'pronouns']
        widgets
    def save(self, commit=True):
        song = super(SongForm, self).save(commit=False)
        song.genre = self.cleaned_data['genre']
        song.subj = self.cleaned_data['subj']
        song.pronouns = self.cleaned_data['pronouns']
        if commit:
            song.save()
        return song
