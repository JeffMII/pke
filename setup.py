from distutils.core import setup

setup(name='pke',
      version='1.8.1',
      description='Python Keyphrase Extraction module',
      author='pke contributors',
      author_email='florian.boudin@univ-nantes.fr',
      license='gnu',
      packages=['pke', 'pke.unsupervised', 'pke.supervised',
                'pke.supervised.feature_based', 'pke.unsupervised.graph_based',
                'pke.unsupervised.statistical', 'pke.supervised.neural_based'],
      url="https://github.com/boudinfl/pke",
      install_requires=[
            'six>=1.15.0, <=1.16.0',
            'spacy>=3.0.0, <=3.2.1',
            'nltk==3.6.3',
            'networkx>=2.4.0, <=2.6.3',
            'numpy==1.16.3',
            'scipy>=1.4.1, <=1.5.4',
            'scikit-learn>=0.22.1, <=1.0.2',
            'unidecode>=1.1.1, <=1.3.2',
            'future==0.18.2',
            'joblib>=0.14.1, <=1.1.0'
      ],
      package_data={'pke': ['models/*.pickle', 'models/*.gz']}
)
