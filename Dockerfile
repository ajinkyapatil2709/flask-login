FROM python
COPY . .
RUN pip install flask
EXPOSE 8091
CMD python login.py



