<template>
    <!-- Main Wrapper -->
    <div class="main-wrapper">
        
        <layouts2></layouts2>
       
        <studentslist></studentslist>
        <!-- Page Wrapper -->
			<div class="page-content">
				
				<div class="container">
					<div class="row">
						<div class="col-lg-12">
						
							<!-- Filter -->
							<div class="showing-list">
								<div class="row">
									<div class="col-lg-6">
										<div class="d-flex align-items-center">
											<div class="view-icons">
												<router-link to="students-grid" class="list-view"><i class="feather-grid"></i></router-link>
												<router-link to="students-list" class="list-view active"><i class="feather-list"></i></router-link>
											</div>
											<div class="show-result">
												<h4>Showing 1-9 of 50 results</h4>
											</div>
										</div>
									</div>
								</div>
							</div>
							<!-- /Filter -->
							
							<div class="row">
							
								<!-- Instructor List -->
								<div class="col-lg-12">
									<div class="student-grid-blk">

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-01.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Charles Dickens</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Brazil</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-02.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Gabriel Palmer</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Italy</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-03.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">James Lemire</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Louisiana</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-04.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Olivia Murphy</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>France</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-05.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Rebecca Swartz</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Iceland</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-06.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Betty Richards</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Louisiana</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-07.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Jeffrey Montgomery</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Brazil</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-08.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Brooke Hayes</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>United States</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-09.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Gertrude Shorter</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Louisiana</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-10.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">David Garza</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Tunisia</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->

										<!-- Row alignment -->
										<div class="row">
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-11.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Vivian Winders</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Louisiana</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
											<div class="col-md-6">
												<div class="student-list flex-fill">
													<div class="student-img">
														<router-link to="student-profile">
															<img class="img-fluid" alt="" src="@/assets/img/students/student-12.jpg">
                                                        </router-link>
													</div>
													<div class="student-content">												
														<h5><router-link to="student-profile">Sean Leon</router-link></h5>
														<h6>Student</h6>
														<div class="student-info">
															<div class="loc-blk d-flex justify-content-center">
																<img src="@/assets/img/students/loc-icon.svg" class="me-1" alt="">
																<p>Spain</p>
															</div>
															<ul class="list-unstyled inline-inline profile-info-social">
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-facebook me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-twitter me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-instagram me-1"></i>
																	</a>
																</li>
																<li class="list-inline-item">
																	<a href="javascript:;">
																		<i class="fa-brands fa-linkedin"></i>
																	</a>
																</li>
															</ul>
														</div>
													</div>
												</div>
											</div>
										</div>
										<!-- /Row alignment -->																				
									</div>
								</div>
								<!-- /Instructor List -->
								
								
							</div>
							
							<pagination></pagination>
							
						</div>
					</div>
				</div>
			</div>
			<!-- /Page Wrapper -->
        <layouts1></layouts1>
       
    </div>
    <!-- /Main Wrapper -->
</template>
