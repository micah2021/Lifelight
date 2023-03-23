{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "a8c76245",
   "metadata": {},
   "outputs": [],
   "source": [
    "import time  # to simulate a real time data, time loop\n",
    "import numpy as np  # np mean, np random\n",
    "import pandas as pd  # read csv, df manipulation\n",
    "import plotly.express as px  # interactive charts\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "136deea0",
   "metadata": {},
   "outputs": [],
   "source": [
    "import streamlit as st  #  data web app development"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "aa5aab70",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataset_url = \"https://docs.google.com/spreadsheets/d/e/2PACX-1vSEIbfyVxix6r_fDNU17bQZzNONVeZYSxPEW3waEve5GmbuSUS5CHKPgVlQkyQo3TQewL9gyodvBdsh/pub?output=csv\"\n",
    "\n",
    "# read csv from a URL\n",
    "st.experimental_memo\n",
    "def get_data() -> pd.DataFrame:\n",
    "    return pd.read_csv(dataset_url)\n",
    "\n",
    "df = get_data()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "39b9f62b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>S/No.</th>\n",
       "      <th>Gender</th>\n",
       "      <th>Ethnicity</th>\n",
       "      <th>Person Nudity</th>\n",
       "      <th>Amount of Skin Exposes</th>\n",
       "      <th>Drawing</th>\n",
       "      <th>Hentai</th>\n",
       "      <th>Neutral</th>\n",
       "      <th>Porn</th>\n",
       "      <th>Sexy</th>\n",
       "      <th>NSFW Label by Model</th>\n",
       "      <th>NSFW Label \\nby \\nHuman</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Female</td>\n",
       "      <td>Black</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0-25%</td>\n",
       "      <td>16.74%</td>\n",
       "      <td>11.49%</td>\n",
       "      <td>16.30%</td>\n",
       "      <td>55.12%</td>\n",
       "      <td>0.35%</td>\n",
       "      <td>True</td>\n",
       "      <td>correct</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Female</td>\n",
       "      <td>Caucasian</td>\n",
       "      <td>Yes</td>\n",
       "      <td>25%-50%</td>\n",
       "      <td>7.65%</td>\n",
       "      <td>26.31%</td>\n",
       "      <td>14.94%</td>\n",
       "      <td>47.57%</td>\n",
       "      <td>3.53%</td>\n",
       "      <td>False</td>\n",
       "      <td>correct</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Male</td>\n",
       "      <td>Mogolian</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0-25%</td>\n",
       "      <td>2.20%</td>\n",
       "      <td>23.03%</td>\n",
       "      <td>6.87%</td>\n",
       "      <td>66.74%</td>\n",
       "      <td>1.15%</td>\n",
       "      <td>True</td>\n",
       "      <td>correct</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Male</td>\n",
       "      <td>Others</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0-25%</td>\n",
       "      <td>22.82%</td>\n",
       "      <td>4.34%</td>\n",
       "      <td>0.62%</td>\n",
       "      <td>72.04%</td>\n",
       "      <td>0.18%</td>\n",
       "      <td>True</td>\n",
       "      <td>correct</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Male</td>\n",
       "      <td>Black</td>\n",
       "      <td>Yes</td>\n",
       "      <td>0-25%</td>\n",
       "      <td>2.26%</td>\n",
       "      <td>17.65%</td>\n",
       "      <td>0.78%</td>\n",
       "      <td>7394.00%</td>\n",
       "      <td>5.37%</td>\n",
       "      <td>True</td>\n",
       "      <td>correct</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   S/No.  Gender  Ethnicity Person Nudity Amount of Skin Exposes Drawing  \\\n",
       "0      1  Female      Black           Yes                  0-25%  16.74%   \n",
       "1      2  Female  Caucasian           Yes                25%-50%   7.65%   \n",
       "2      3    Male   Mogolian           Yes                  0-25%   2.20%   \n",
       "3      4    Male     Others           Yes                  0-25%  22.82%   \n",
       "4      5    Male      Black           Yes                  0-25%   2.26%   \n",
       "\n",
       "   Hentai Neutral      Porn   Sexy  NSFW Label by Model  \\\n",
       "0  11.49%  16.30%    55.12%  0.35%                 True   \n",
       "1  26.31%  14.94%    47.57%  3.53%                False   \n",
       "2  23.03%   6.87%    66.74%  1.15%                 True   \n",
       "3   4.34%   0.62%    72.04%  0.18%                 True   \n",
       "4  17.65%   0.78%  7394.00%  5.37%                 True   \n",
       "\n",
       "  NSFW Label \\nby \\nHuman  \n",
       "0                 correct  \n",
       "1                 correct  \n",
       "2                 correct  \n",
       "3                 correct  \n",
       "4                 correct  "
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "a0a3e162",
   "metadata": {},
   "outputs": [],
   "source": [
    "st.set_page_config(\n",
    "    page_title=\"Real-Time Data Science Dashboard\",\n",
    "    page_icon=\"✅\",\n",
    "    layout=\"wide\",\n",
    ")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "f169ff45",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.title(\"Real-Time / Live Data Science Dashboard\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "3e900f6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "job_filter = st.selectbox(\"Select the Job\", pd.unique(df[\"Gender\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "b5a59eef",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[df[\"Gender\"] == job_filter]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "95d32dc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig_col1, fig_col2 = st.columns(2)\n",
    "\n",
    "with fig_col1:\n",
    "    st.markdown(\"### First Chart\")\n",
    "    fig = px.density_heatmap(\n",
    "        data_frame=df, y=\"Ethnicity\", x=\"Gender\"\n",
    "    )\n",
    "    st.write(fig)\n",
    "   \n",
    "with fig_col2:\n",
    "    st.markdown(\"### Second Chart\")\n",
    "    fig2 = px.histogram(data_frame=df, x=\"Porn\")\n",
    "    st.write(fig2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "e28e72ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "DeltaGenerator(_root_container=0, _provided_cursor=None, _parent=None, _block_type=None, _form_data=None)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "st.markdown(\"### Detailed Data View\")\n",
    "st.dataframe(df)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
